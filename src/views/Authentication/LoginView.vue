<script setup>
import { RouterLink } from 'vue-router'
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

const router = useRouter()
const store = useStore()

const loading = ref(false)
const loginFormError = ref('')
const loginFormData = ref({
  email: '',
  password: ''
})

const isAuthenticated = computed(() => {
  return store.state.auth.status.isAuthenticated
})

onMounted(async () => {
  if (isAuthenticated.value) {
    router.push('/dashboard')
  }
})

function login() {
  loading.value = true

  store
    .dispatch('auth/login', loginFormData.value)
    .then(() => {
      router.push('/')
    })
    .catch((error) => {
      window.scrollTo(0, 0)
      loading.value = false
      loginFormError.value = error.response.data.detail || error.toString()
    })
}
</script>

<template>
  <main class="w-100 min-vh-100 d-flex justify-content-center">
    <form @submit.prevent="login" class="d-flex flex-column p-3 my-auto mx-3">
      <h2 class="text-center text-primary mb-4">Login</h2>
      <!-- Email input -->
      <div class="form-outline mb-3">
        <label class="form-label" for="form2Example1">Email address</label>
        <input
          type="email"
          id="form2Example1"
          class="form-control py-2"
          placeholder="name@example.com"
          v-model="loginFormData.email"
        />
      </div>

      <!-- Password input -->
      <div class="form-outline mb-3">
        <label class="form-label" for="form2Example2">Password</label>
        <input
          type="password"
          id="form2Example2"
          class="form-control py-2"
          v-model="loginFormData.password"
        />
        <p v-if="loginFormError" class="m-0 text-danger">
          {{ loginFormError }}
        </p>
      </div>

      <div class="row mb-4 text-center">
        <RouterLink to="/forgot-password">Forgot password?</RouterLink>
      </div>

      <!-- Submit button -->
      <button type="submit" class="btn btn-primary btn-block mb-4" :class="{ disabled: loading }">
        <div v-if="loading" class="spinner-border spinner-border-sm text-light" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
        <template v-else> Sign in </template>
      </button>

      <!-- Register buttons -->
      <div class="text-center">
        <p>Not a member? <RouterLink to="/register">Register</RouterLink></p>
      </div>
    </form>
  </main>
</template>

<style scoped>
form {
  width: 500px;
  min-width: auto;
  height: auto;
  border: 1px solid rgba(0, 0, 0, 0.2);
}
</style>
