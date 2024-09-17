<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <main class="w-100 min-vh-100 d-flex justify-content-center">
    <form class="d-flex flex-column p-3 my-5 mx-3">
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
            required
          />
        </div>
        <div class="col-md-6 col-12 form-outline">
          <label class="form-label" for="form2Example2">Firstname</label>
          <input
            type="text"
            id="form2Example2"
            class="form-control py-2"
            placeholder="John"
            required
          />
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
          required
        />
      </div>
      <!-- Password input -->
      <div class="row">
        <div class="col col-md-6 col-12 form-outline mb-4">
          <label class="form-label" for="form2Example2">Password</label>
          <input type="password" id="form2Example3" class="form-control py-2" required />
        </div>
        <div class="col col-md-6 col-12 form-outline mb-4">
          <label class="form-label" for="form2Example2">Confirm Password</label>
          <input type="password" id="form2Example4" class="form-control py-2" required />
        </div>
      </div>

      <!-- Submit button -->
      <button
        type="button"
        data-mdb-button-init
        data-mdb-ripple-init
        class="btn btn-primary btn-block mb-4"
      >
        Sign up
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
