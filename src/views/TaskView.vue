<script setup>
import DashTopBar from '@/components/DashTopBar.vue'
import { RouterLink, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { computed, ref, onMounted } from 'vue'
import ProjectService from '../services/project-service.js'

const store = useStore()
const router = useRouter()

const projectTasks = ref([])

const props = defineProps({
  project_id: {
    type: Number,
    required: true
  }
})

const isAuthenticated = computed(() => {
  return store.state.auth.status.isAuthenticated
})

onMounted(async () => {
  if (!isAuthenticated.value) {
    router.push('/login')
  }

  await getProjectTasks(props.project_id)
})

async function getProjectTasks(project_id) {
  try {
    const data = await ProjectService.getTasks(project_id)
    projectTasks.value = data
  } catch (error) {
    if (error && error.response && error.response.status === 404) {
      router.replace('/')
    }
  }
}

function formatDate(backendDateString) {
  const date = new Date(backendDateString)

  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  }

  return date.toLocaleString('fr-FR', options)
}
</script>
<template>
  <div>
    <!-- Page Wrapper -->
    <div id="wrapper">
      <!-- <DashSideBar /> -->
      <!-- Content Wrapper -->
      <div id="content-wrapper" class="d-flex flex-column min-vh-100">
        <!-- Main Content -->
        <div id="content">
          <DashTopBar />

          <!-- Begin Page Content -->
          <div class="container-fluid">
            <!-- Page Heading -->
            <div class="d-sm-flex align-items-center justify-content-between mb-4">
              <div>
                <h1 class="h3 mb-0 text-gray-800">
                  <RouterLink to="/dashboard" class="text-decoration-underline"
                    >Projects</RouterLink
                  >
                  / Tasks
                </h1>
                <p class="mb-0">Click on a task row to view more details about the task.</p>
              </div>
              <button
                class="d-sm-inline-block btn btn-sm btn-primary shadow-sm"
                data-bs-toggle="modal"
                data-bs-target="#taskModal"
              >
                <i class="fas fa-plus-circle fa-sm text-white-50"></i> New Task
              </button>
            </div>

            <!-- DataTales Example -->
            <div class="card shadow mb-4">
              <div class="card-body">
                <select
                  class="form-select form-select-sm mb-3 py-2 ms-auto"
                  aria-label="Small select example"
                >
                  <option selected>Sort by</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>
                <div class="table-responsive">
                  <table
                    class="table table-bordered table-hover"
                    id="dataTable"
                    width="100%"
                    cellspacing="0"
                  >
                    <thead>
                      <tr>
                        <th class="bg-primary text-light">#</th>
                        <th class="bg-primary text-light">Title</th>
                        <th class="bg-primary text-light">Priority</th>
                        <th class="bg-primary text-light">Assigned To</th>
                        <th class="bg-primary text-light">Start date</th>
                        <th class="bg-primary text-light">Due Date</th>
                        <th class="bg-primary text-light">Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(task, i) in projectTasks" :key="i">
                        <td>{{ i }}</td>
                        <td>{{ task?.description }}</td>
                        <td>{{ task?.description }}</td>
                        <td>
                          <ul v-if="task?.members.length > 0">
                            <li v-for="member in task?.members" :key="member.id">
                              {{ member.last_name + member.first_name }}
                            </li>
                          </ul>
                          <span v-else>None</span>
                        </td>
                        <td>{{ formatDate(task?.start_date) }}</td>
                        <td>{{ formatDate(task?.end_date) }}</td>
                        <td>
                          <span v-if="task?.status == 'DONE'" class="p-2 bg-success">
                            {{ task?.status }}
                          </span>
                          <span v-else-if="task?.status == 'IN_PROG'" class="p-2 bg-warning">
                            {{ task?.status }}
                          </span>
                          <span v-else-if="task?.status == 'TODO'" class="p-2 bg-secondary">
                            {{ task?.status }}
                          </span>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
          <!-- /.container-fluid -->
        </div>
        <!-- End of Main Content -->
      </div>
      <!-- End of Content Wrapper -->
    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
      <i class="fas fa-angle-up"></i>
    </a>
  </div>

  <!-- Task Modal-->
  <div
    class="modal fade"
    id="taskModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="exampleModalLabel"
    data-bs-backdrop="static"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-xl modal-dialog-scrollable" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col col-md-6 col-12 form-outline mb-3">
              <label class="form-label" for="form2Example2">Title</label>
              <input
                type="text"
                id="form2Example3"
                class="form-control py-2"
                required
                placeholder="Project..."
              />
            </div>
            <div class="col col-md-6 col-12 form-outline mb-3">
              <label class="form-label" for="form2Example2">Description</label>
              <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
            </div>
          </div>
          <div></div>
          <div class="row">
            <div class="col col-md-6 col-12 form-outline mb-3">
              <label class="form-label" for="form2Example4">Start date</label>
              <input type="date" id="form2Example4" class="form-control py-2" required />
            </div>
            <div class="col col-md-6 col-12 form-outline mb-3">
              <label class="form-label" for="form2Example4">Start date</label>
              <input type="date" id="form2Example4" class="form-control py-2" required />
            </div>
          </div>
          <div class="row">
            <div class="col col-md-6 col-12 form-outline mb-3">
              <label class="form-label">Priority</label>
              <select class="form-select w-100" aria-label="Default select example">
                <option selected>Open this select menu</option>
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
              </select>
            </div>
            <div class="col col-md-6 col-12 form-outline mb-3">
              <label class="form-label">Status</label>
              <select class="form-select w-100" aria-label="Default select example">
                <option selected>Open this select menu</option>
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
              </select>
            </div>
          </div>
          <div class="row">
            <div class="col col-md-6 col-12 form-outline mb-3">
              <label class="form-label">Member</label>
              <select class="form-select mb-3" multiple aria-label="Multiple select example">
                <option selected>Open this select menu</option>
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
              </select>
              <!-- <table class="table" id="dataTable" width="100%" cellspacing="0">
                <tbody>
                  <tr>
                    <td class="p-0">Edinburgh</td>
                    <td class="p-0">
                      <button class="d-sm-inline-block btn btn-sm btn-white">
                        <i class="fas fa-remove fa-sm text-danger"></i>
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table> -->
            </div>
            <div class="col col-md-6 col-12 form-outline mb-3">
              <label class="form-label" for="form2Example2">Comments</label>
              <textarea
                class="form-control"
                id="exampleFormControlTextarea1"
                rows="3"
                placeholder="Write a comment"
              ></textarea>
              <button class="d-block btn btn-dark mt-3 ml-auto" type="button" data-dismiss="modal">
                Send
              </button>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a class="btn btn-primary" href="login.html">Save</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@import '../assets/sb-admin-2.css';

.card .card-body .form-select {
  display: flex;
  align-items: center;
  max-width: 300px;
}

.table-hover:hover {
  cursor: pointer;
}

.table-hover:hover thead tr {
  cursor: default;
}
</style>
