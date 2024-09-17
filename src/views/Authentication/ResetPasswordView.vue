<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <main class="w-100 min-vh-100 d-flex justify-content-center">
    <form class="d-flex flex-column p-3 my-auto mx-3">
      <h2 class="text-center text-primary mb-2">Reset Password</h2>
      <span class="text-center mb-4"
        >Enter the new password you would like to use for your account</span
      >
      <!-- Email input -->
      <div data-mdb-input-init class="form-outline mb-3">
        <label class="form-label" for="form2Example1">Email address</label>
        <input
          type="email"
          id="form2Example1"
          class="form-control py-2"
          placeholder="name@example.com"
          readonly
        />
      </div>
      <!-- Password input -->
      <div data-mdb-input-init class="form-outline mb-3">
        <label class="form-label" for="form2Example2">New Password</label>
        <input type="password" id="form2Example2" class="form-control py-2" />
      </div>
      <div data-mdb-input-init class="form-outline mb-3">
        <label class="form-label" for="form2Example3">Confirm Password</label>
        <input type="password" id="form2Example3" class="form-control py-2" />
      </div>

      <!-- Submit button -->
      <button
        type="button"
        data-mdb-button-init
        data-mdb-ripple-init
        class="btn btn-primary btn-block mb-4"
      >
        Reset Password
      </button>
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
