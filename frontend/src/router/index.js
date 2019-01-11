import Vue from 'vue'
import Router from 'vue-router'
import RoomManage from '@/components/RoomManage'
import NewRoom from '@/components/NewRoom'
import TeacherIndex from '@/components/TeacherIndex'
import PickStuAudit from '@/components/PickStuAudit'
import PickStuAccepted from '@/components/PickStuAccepted'
import stuIndex from '@/components/stuIndex'
import teachingRoom from '@/components/teachingRoom'
import Login from '@/components/Login'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/TeacherIndex',
      name: 'TeacherIndex',
      component: TeacherIndex
    },
    {
      path: '/RoomManage',
      name: 'RoomManage',
      component: RoomManage
    },
    {
      path: '/NewRoom',
      name: 'NewRoom',
      component: NewRoom
    },
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
      path: '/stuIndex',
      name: 'stuIndex',
      component: stuIndex
    },
    {
      path: '/teachingRoom',
      name: 'teachingRoom',
      component: teachingRoom
    },
    {
      path: '/Login',
        name: 'Login',
      component: Login
    }
  ]
})
