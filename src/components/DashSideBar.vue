<script setup>
import { RouterLink } from 'vue-router'
</script>
<template>
  <!-- Sidebar -->
  <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">
    <!-- Divider -->
    <hr class="sidebar-divider my-0" />

    <!-- Nav Item - Dashboard -->
    <li class="nav-item active">
      <RouterLink class="nav-link" to="/dashboard">
        <i class="fas fa-clipboard-list"></i>
        <span>My projects</span></RouterLink
      >
    </li>
    <!-- Divider -->
    <hr class="sidebar-divider" />
  </ul>
  <!-- End of Sidebar -->
</template>
