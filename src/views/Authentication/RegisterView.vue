<script setup>
import { RouterLink } from 'vue-router'
import { ref, computed, onMounted } from 'vue'
import AuthenticationService from '@/services/authentication-service.js'

import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

const router = useRouter()
const store = useStore()

const isAuthenticated = computed(() => {
  return store.state.auth.status.isAuthenticated
})

const registerFormData = ref({
  first_name: null,
  last_name: null,
  email: null,
  password: null,
  re_password: null
})
const registerFormError = ref(null)
const loading = ref(false)

onMounted(async () => {
  if (isAuthenticated.value) {
    router.push('/dashboard')
  }
})

async function register() {
  loading.value = true
  await AuthenticationService.register(registerFormData.value)
    .then(() => {
      setTimeout(() => {
        loading.value = false
        formatInput()
        router.push('/login')
      }, 300)
    })
    .catch((error) => {
      console.log(error)
      setTimeout(() => {
        loading.value = false
        if (error && error.response && error.response.status === 400) {
          registerFormError.value = error.response.data
        }
      }, 300)
    })
}

function formatInput() {
  registerFormData.value = {
    first_name: null,
    last_name: null,
    email: null,
    password: null,
    re_password: null
  }
}
</script>

<template>
  <main class="w-100 min-vh-100 d-flex justify-content-center">
    <form @submit.prevent="register" class="d-flex flex-column p-3 my-5 mx-3">
      <h2 class="text-center text-primary mb-2">Register</h2>
      <span class="text-center mb-4">Register now to access more</span>
      <!-- Name input -->
      <div class="row row-cols-2 mb-3">
        <div class="col-md-6 col-12 form-outline">
          <label class="form-label" for="form2Example1">Lastname</label>
          <input
            type="text"
            id="form2Example1"
            class="form-control py-2"
            placeholder="DOE"
            v-model="registerFormData.last_name"
            required
          />
          <p class="m-0 text-danger" v-if="registerFormError && registerFormError.last_name">
            {{ registerFormError.last_name[0] }}
          </p>
        </div>
        <div class="col-md-6 col-12 form-outline">
          <label class="form-label" for="form2Example2">Firstname</label>
          <input
            type="text"
            id="form2Example2"
            class="form-control py-2"
            placeholder="John"
            v-model="registerFormData.first_name"
            required
          />
          <p class="m-0 text-danger" v-if="registerFormError && registerFormError.last_name">
            {{ registerFormError.last_name[0] }}
          </p>
        </div>
      </div>
      <!-- Email input -->
      <div class="form-outline mb-3">
        <label class="form-label" for="form2Example3">Email address</label>
        <input
          type="email"
          id="form2Example3"
          class="form-control py-2"
          placeholder="name@example.com"
          v-model="registerFormData.email"
          required
        />
        <p class="m-0 text-danger" v-if="registerFormError && registerFormError.email">
          {{ registerFormError.email[0] }}
        </p>
      </div>
      <!-- Password input -->
      <div class="row">
        <div class="col col-md-6 col-12 form-outline mb-4">
          <label class="form-label" for="form2Example4">Password</label>
          <input
            type="password"
            id="form2Example4"
            class="form-control py-2"
            required
            v-model="registerFormData.password"
          />
          <p class="m-0 text-danger" v-if="registerFormError && registerFormError.password">
            {{ registerFormError.password[0] }}
          </p>
          <p
            class="m-0 mt-2 text-danger"
            v-else-if="registerFormError && registerFormError.non_field_errors"
          >
            {{ registerFormError.non_field_errors[0] }}
          </p>
        </div>
        <div class="col col-md-6 col-12 form-outline mb-4">
          <label class="form-label" for="form2Example5">Confirm Password</label>
          <input
            type="password"
            id="form2Example5"
            class="form-control py-2"
            required
            v-model="registerFormData.re_password"
          />
        </div>
      </div>

      <!-- Submit button -->
      <button
        type="submit"
        data-mdb-button-init
        data-mdb-ripple-init
        class="btn btn-primary btn-block mb-4"
        :class="{ disabled: loading }"
      >
        <div v-if="loading" class="spinner-border spinner-border-sm text-light" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
        <template v-else> Sign up </template>
      </button>

      <!-- Register buttons -->
      <div class="text-center">
        <p>Already a member? <RouterLink to="/login">Login</RouterLink></p>
      </div>
    </form>
  </main>
</template>

<style scoped>
form {
  width: 800px;
  min-width: auto;
  height: auto;
  border: 1px solid rgba(0, 0, 0, 0.2);
}
</style>
