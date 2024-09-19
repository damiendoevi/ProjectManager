<script setup>
import { RouterView, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import eventBus from './common/event-bus'
import { onMounted, onBeforeUnmount } from 'vue'

const router = useRouter()
const store = useStore()

function logOut() {
  store.dispatch('auth/logout')
  router.push('/login')
}

onMounted(async () => {
  eventBus.on('logout', () => {
    logOut()
  })
})

onBeforeUnmount(() => {
  eventBus.remove('logout')
})
</script>

<template>
  <RouterView />
</template>
