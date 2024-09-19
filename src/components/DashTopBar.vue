<script setup>
import { RouterLink, useRouter } from 'vue-router'
import AuthenticationService from '../services/authentication-service.js'
import { useStore } from 'vuex'
import { ref, onMounted } from 'vue'

const router = useRouter()
const store = useStore()

const loading = ref(false)

const user = ref(null)

onMounted(async () => {
  editProfile()
})

async function editProfile() {
  try {
    const data = await AuthenticationService.editProfile()
    user.value = data
  } catch (error) {
    return
  }
}

function handleLogout() {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    store.dispatch('auth/logout').then(async () => {
      await closeModal()
      router.push('/login')
    })
  }, 2000)
}

async function closeModal() {
  const modal = document.getElementById('logoutModal')
  const bootstrapModal = bootstrap.Modal.getInstance(modal)

  bootstrapModal.hide()
}
</script>
<template>
  <!-- Topbar -->
  <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">
    <!-- Topbar Search -->
    <form class="d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search">
      <div class="input-group">
        <input
          type="text"
          class="form-control bg-light border-0 small"
          placeholder="Search projects..."
          aria-label="Search"
          aria-describedby="basic-addon2"
        />
        <div class="input-group-append">
          <button class="btn btn-primary" type="button">
            <i class="fas fa-search fa-sm"></i>
          </button>
        </div>
      </div>
    </form>

    <!-- Topbar Navbar -->
    <ul class="navbar-nav ml-auto">
      <!-- Nav Item - Alerts -->
      <li class="nav-item dropdown no-arrow mx-1">
        <a
          class="nav-link dropdown-toggle"
          href="#"
          id="alertsDropdown"
          role="button"
          data-bs-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
        >
          <i class="fas fa-bell fa-fw"></i>
          <!-- Counter - Alerts -->
          <span class="badge badge-danger badge-counter">3+</span>
        </a>
        <!-- Dropdown - Alerts -->
        <div
          class="dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in"
          aria-labelledby="alertsDropdown"
        >
          <h6 class="dropdown-header">Alerts Center</h6>
          <a class="dropdown-item d-flex align-items-center" href="#">
            <div class="mr-3">
              <div class="icon-circle bg-primary">
                <i class="fas fa-file-alt text-white"></i>
              </div>
            </div>
            <div>
              <div class="small text-gray-500">December 12, 2019</div>
              <span class="font-weight-bold">A new monthly report is ready to download!</span>
            </div>
          </a>
          <a class="dropdown-item d-flex align-items-center" href="#">
            <div class="mr-3">
              <div class="icon-circle bg-success">
                <i class="fas fa-donate text-white"></i>
              </div>
            </div>
            <div>
              <div class="small text-gray-500">December 7, 2019</div>
              $290.29 has been deposited into your account!
            </div>
          </a>
          <a class="dropdown-item d-flex align-items-center" href="#">
            <div class="mr-3">
              <div class="icon-circle bg-warning">
                <i class="fas fa-exclamation-triangle text-white"></i>
              </div>
            </div>
            <div>
              <div class="small text-gray-500">December 2, 2019</div>
              Spending Alert: We've noticed unusually high spending for your account.
            </div>
          </a>
          <a class="dropdown-item text-center small text-gray-500" href="#">Show All Alerts</a>
        </div>
      </li>

      <div class="topbar-divider d-none d-sm-block"></div>

      <!-- Nav Item - User Information -->
      <li class="nav-item dropdown no-arrow">
        <a
          class="nav-link dropdown-toggle"
          href="#"
          id="userDropdown"
          role="button"
          data-bs-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
        >
          <span class="mr-2 d-none d-lg-inline text-gray-600 small">{{ user?.last_name }}</span>
          <div
            class="img-profile rounded-circle"
            style="height: 40px; width: 40px; background-color: rgba(0, 0, 0, 0.1)"
          ></div>
        </a>
        <!-- Dropdown - User Information -->
        <div
          class="dropdown-menu dropdown-menu-left shadow animated--grow-in"
          aria-labelledby="userDropdown"
        >
          <RouterLink class="dropdown-item" to="/">
            <i class="fas fa-arrow-left fa-sm fa-fw mr-2 text-gray-400"></i>
            Home
          </RouterLink>
          <div class="dropdown-divider"></div>
          <RouterLink
            class="dropdown-item"
            to="#"
            data-bs-toggle="modal"
            data-bs-target="#logoutModal"
          >
            <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
            Logout
          </RouterLink>
        </div>
      </li>
    </ul>
  </nav>
  <!-- End of Topbar -->

  <!-- Logout Modal-->
  <div
    class="modal fade"
    id="logoutModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          Are you sure you want to log out? If yes, please click on Logout to confirm.
        </div>
        <div class="modal-footer">
          <RouterLink
            @click.prevent="handleLogout"
            class="btn btn-primary"
            :class="{ disabled: loading }"
            to="#"
            >Logout</RouterLink
          >
        </div>
      </div>
    </div>
  </div>
</template>
