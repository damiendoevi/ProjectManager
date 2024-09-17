<script setup>
import DashTopBar from '@/components/DashTopBar.vue'

function getBorderStyle(index) {
  // Use the index to generate a different shade (hue)
  const hue = (index * 60) % 360
  const color = `hsl(${hue}, 70%, 50%)`
  return {
    borderLeft: `4px solid ${color}`
  }
}

function getTextStyle(index) {
  // Use the index to generate a different shade (hue)
  const hue = (index * 60) % 360
  const color = `hsl(${hue}, 70%, 50%)`
  return {
    color: `${color}`
  }
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
              <h1 class="h3 mb-0 text-gray-800">Projects</h1>
              <button
                class="d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm"
                data-bs-toggle="modal"
                data-bs-target="#projectModal"
              >
                <i class="fas fa-plus-circle fa-sm text-white-50"></i> New Project
              </button>
            </div>

            <!-- Content Row -->
            <div class="row">
              <div v-for="i in 6" :key="i" class="col-md-6 mb-4">
                <RouterLink
                  to="/dashboard/projects/1/tasks"
                  class="card shadow h-100 py-2 text-decoration-none"
                  id="project_card"
                  :style="getBorderStyle(i)"
                >
                  <div class="card-body">
                    <div class="row no-gutters align-items-center">
                      <div class="col">
                        <div class="text-xs font-weight-bold mb-1" :style="getTextStyle(i)">
                          Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        </div>
                      </div>
                    </div>
                  </div>
                </RouterLink>
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
    id="projectModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
    data-bs-backdrop="static"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Project</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="form-outline mb-3">
            <label class="form-label" for="form2Example1">Name</label>
            <input
              type="text"
              id="form2Example1"
              class="form-control py-2"
              placeholder="Project..."
            />
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
          <a class="btn btn-primary" href="login.html">Save</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@import '../assets/sb-admin-2.css';

#project_card:hover {
  background-color: rgba(0, 0, 0, 0.01) !important;
}
</style>
