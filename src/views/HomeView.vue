<script setup>
import { RouterLink } from 'vue-router'
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

const router = useRouter()
const store = useStore()

const isAuthenticated = computed(() => {
  return store.state.auth.status.isAuthenticated
})

function goToDashboard() {
  if (isAuthenticated.value) {
    router.push('/dashboard')
  } else {
    router.push('/login')
  }
}
</script>

<template>
  <main class="masthead d-flex align-items-center">
    <div class="container px-4 px-lg-5 text-center">
      <h1 class="mb-1 text-secondary">Simplify Your Project Management</h1>
      <h3 class="mb-5">
        <em>Effortlessly manage your projects, tasks, and teams in one place</em>
      </h3>
      <RouterLink @click.prevent="" to="#" class="btn btn-primary" @click="goToDashboard"
        >Discover How</RouterLink
      >
    </div>
  </main>
</template>

<style scoped>
.masthead {
  min-height: 30rem;
  position: relative;
  display: table;
  width: 100%;
  height: auto;
  padding-top: 8rem;
  padding-bottom: 8rem;
  background: linear-gradient(90deg, rgba(0, 0, 0, 0.1) 0%, rgba(0, 0, 0, 0.8) 100%),
    url('../assets/img/bloc_note_2.png');
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 100vh;
}
.masthead h1,
.masthead .h1 {
  font-size: 2rem;
}

h1,
h3 {
  color: black !important;
}

@media (min-width: 992px) {
  .masthead {
    height: 100vh;
  }
  .masthead h1,
  .masthead .h1 {
    font-size: 4rem;
  }
}
</style>
