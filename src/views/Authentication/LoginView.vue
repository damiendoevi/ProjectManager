<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <main class="w-100 min-vh-100 d-flex justify-content-center">
    <form class="d-flex flex-column p-3 my-auto mx-3">
      <h2 class="text-center text-primary mb-4">Login</h2>
      <!-- Email input -->
      <div class="form-outline mb-3">
        <label class="form-label" for="form2Example1">Email address</label>
        <input
          type="email"
          id="form2Example1"
          class="form-control py-2"
          placeholder="name@example.com"
        />
      </div>

      <!-- Password input -->
      <div class="form-outline mb-3">
        <label class="form-label" for="form2Example2">Password</label>
        <input type="password" id="form2Example2" class="form-control py-2" />
      </div>

      <div class="row mb-4 text-center">
        <RouterLink to="/forgot-password">Forgot password?</RouterLink>
      </div>

      <!-- Submit button -->
      <button
        type="button"
        data-mdb-button-init
        data-mdb-ripple-init
        class="btn btn-primary btn-block mb-4"
      >
        Sign in
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
