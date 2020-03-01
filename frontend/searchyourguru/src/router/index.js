import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import Verification from '../views/Verification.vue'
import PasswordReset from '../views/PasswordReset.vue'
import Dashboard from '../views/Dashboard.vue'
import Search from '../views/Search.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      title: 'SearchYourGuru Home',
      metaTags: [
        {
          name: 'description',
          content:
            'SearchYourGuru lets tutor to post tution details and student to search for a tution'
        },
        {
          property: 'og:type',
          content: 'website'
        },
        {
          property: 'og:site_name',
          content: 'SearchYourGuru'
        },
        {
          property: 'og:url',
          content: 'https://searchyourguru.com'
        }
      ]
    },
    beforeEnter(to, from, next) {
      if (store.getters.is_user_tutor) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/search/',
    name: 'search',
    component: Search,
    meta: {
      title: 'Tuitions & Tutors - SearchYourGuru',
      metaTags: [
        {
          name: 'description',
          content:
            'SearchYourGuru lets students to search tutions for a subject'
        },
        {
          property: 'og_type',
          content: 'website'
        },
        {
          property: 'og:site_name',
          content: 'SearchYourGuru'
        },
        {
          property: 'og:url',
          content: 'https://searchyourguru.com'
        }
      ]
    },
    beforeEnter(to, from, next) {
      if (store.getters.is_user_tutor) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/login/',
    name: 'login',
    component: Login,
    meta: {
      title: 'Login - SearchYourGuru',
      metaTags: [
        {
          name: 'description',
          content: 'Login, Signup - SearchYourGuru'
        },
        {
          property: 'og_type',
          content: 'website'
        },
        {
          property: 'og:site_name',
          content: 'SearchYourGuru'
        },
        {
          property: 'og:url',
          content: 'https://searchyourguru.com'
        }
      ]
    },
    beforeEnter(to, from, next) {
      if (store.getters.is_loggedin) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/signup/',
    name: 'signup',
    component: Signup,
    meta: {
      title: 'Signup, Registration - Searchyourguru',
      metaTags: [
        {
          name: 'description',
          content:
            'Register as tutor or student, create an account - SearchYourGuru'
        },
        {
          property: 'og_type',
          content: 'website'
        },
        {
          property: 'og:site_name',
          content: 'SearchYourGuru'
        },
        {
          property: 'og:url',
          content: 'https://searchyourguru.com'
        }
      ]
    },
    beforeEnter(to, from, next) {
      if (store.getters.is_loggedin) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/verification/',
    name: 'verification',
    component: Verification,
    meta: {
      title: 'SearchYourGuru Verification',
      metaTags: [
        {
          name: 'description',
          content: 'Email Verification - SearchYourGuru'
        },
        {
          property: 'og_type',
          content: 'website'
        },
        {
          property: 'og:site_name',
          content: 'SearchYourGuru'
        },
        {
          property: 'og:url',
          content: 'https://searchyourguru.com'
        }
      ]
    },
    beforeEnter(to, from, next) {
      if (store.getters.is_loggedin) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/password-reset/',
    name: 'password_reset',
    component: PasswordReset,
    meta: {
      title: 'Forgot Password - SearchYourGuru',
      metaTags: [
        {
          name: 'description',
          content: 'Reset your password, forgot password - SearchYourGuru'
        },
        {
          property: 'og_type',
          content: 'website'
        },
        {
          property: 'og:site_name',
          content: 'SearchYourGuru'
        },
        {
          property: 'og:url',
          content: 'https://searchyourguru.com'
        }
      ]
    },
    beforeEnter(to, from, next) {
      if (store.getters.is_loggedin) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/dashboard/',
    name: 'dashboard',
    component: Dashboard,
    meta: {
      title: 'Dashboard - SearchYourGuru',
      metaTags: [
        {
          name: 'description',
          content: 'Manage Tuitions, account - SearchYourGuru'
        },
        {
          property: 'og:type',
          content: 'website'
        },
        {
          property: 'og:site_name',
          content: 'SearchYourGuru'
        }
      ]
    },
    beforeEnter(to, from, next) {
      if (!store.getters.is_loggedin) next('/login/')
      else next()
    }
  }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

router.beforeEach((to, from, next) => {
  const nearestWithTitle = to.matched
    .slice()
    .reverse()
    .find(r => r.meta && r.meta.title)
  const nearestWithMeta = to.matched
    .slice()
    .reverse()
    .find(r => r.meta && r.meta.metaTags)

  if (nearestWithTitle) document.title = nearestWithTitle.meta.title

  Array.from(
    document.querySelectorAll('[data-vue-router-controlled]')
  ).map(el => el.parentNode.removeChild(el))

  if (!nearestWithMeta) return next()

  nearestWithMeta.meta.metaTags
    .map(tagDef => {
      const tag = document.createElement('meta')

      Object.keys(tagDef).forEach(key => {
        tag.setAttribute(key, tagDef[key])
      })

      tag.setAttribute('data-vue-router-controlled', '')

      return tag
    })
    .forEach(tag => document.head.appendChild(tag))
  next()
})

export default router
