<script setup>
import DashTopBar from '@/components/DashTopBar.vue'
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
                      <tr v-for="i in 6" :key="i">
                        <td>{{ i }}</td>
                        <td>Lorem ipsum dolor sit amet consectetur adipisicing elit.</td>
                        <td>System Architect</td>
                        <td>Edinburgh</td>
                        <td>61</td>
                        <td>2011/04/25</td>
                        <td>$320,800</td>
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
              <table class="table" id="dataTable" width="100%" cellspacing="0">
                <tbody>
                  <tr v-for="i in 6" :key="i">
                    <td class="p-0">Edinburgh</td>
                    <td class="p-0">
                      <button class="d-sm-inline-block btn btn-sm btn-white">
                        <i class="fas fa-remove fa-sm text-danger"></i>
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
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
