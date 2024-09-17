import { createRouter, createWebHistory } from 'vue-router'
import RegisterView from '../views/Authentication/RegisterView.vue'
import LoginView from '../views/Authentication/LoginView.vue'
import ForgotPasswordView from '../views/Authentication/ForgotPasswordView.vue'
import ResetPasswordView from '@/views/Authentication/ResetPasswordView.vue'
import HomeView from '@/views/HomeView.vue'
import DashboardView from '@/views/DashboardView.vue'
import TaskView from '@/views/TaskView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: {
        title: 'Login'
      }
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
      meta: {
        title: 'Register'
      }
    },
    {
      path: '/forgot-password',
      name: 'forgot-password',
      component: ForgotPasswordView,
      meta: {
        title: 'Forgot Password'
      }
    },
    {
      path: '/reset-password',
      name: 'reset-password',
      component: ResetPasswordView,
      meta: {
        title: 'Reset Password'
      }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      meta: {
        title: 'Dashboard'
      }
    },
    {
      path: '/dashboard/projects/:project_id/tasks',
      name: 'project-tasks',
      component: TaskView,
      props: (route) => ({
        project_id: route.params.project_id
      }),
      meta: {
        title: 'Tasks'
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Authentication/LoginView.vue')
    }
  ]
})

export default router
