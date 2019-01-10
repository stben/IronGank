import Vue from 'vue'
import Router from 'vue-router'
import PickStuAudit from '@/components/PickStuAudit'
import PickStuAccepted from '@/components/PickStuAccepted'
import Login from '@/components/Login'
import BanStu from '@/components/BanStu'
import timeTable from '@/components/timeTable'
import AllRoom from '@/components/AllRoom'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/teacher/pickstu/audit',
      name: 'PickStuAudit',
      component: PickStuAudit
    },
    {
      path: '/teacher/pickstu/accepted',
      name: 'PickStuAccepted',
      component: PickStuAccepted
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/NewRoom',
      name: 'NewRoom',
      component: NewRoom
    },
            {
      path: '/AllRoom',
      name: 'AllRoom',
      component: AllRoom
    },
    {
      path: '/teacher/banstu',
      name: 'BanStu',
      component: BanStu
    },
    {
      path: '/teacher/timeTable',
      name: 'timeTable',
      component: timeTable
    }
  ]
})
