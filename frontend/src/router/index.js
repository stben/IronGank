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
import BanStu from '@/components/BanStu'
import timeTable from '@/components/timeTable'
import register from '@/components/register'
import pickTeacherAudit from '@/components/pickTeacherAudit'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/teacher/index',
      name: 'TeacherIndex',
      component: TeacherIndex
    },
    {
      path: '/teacher/roomManage',
      name: 'RoomManage',
      component: RoomManage
    },
    {
      path: '/teacher/newRoom',
      name: 'NewRoom',
      component: NewRoom
    },
    {
      path: '/teacher/pickStudent/audit',
      name: 'PickStuAudit',
      component: PickStuAudit
    },
    {
      path: '/teacher/pickStudent/accepted',
      name: 'PickStuAccepted',
      component: PickStuAccepted
    },
    {
      path: '/student/index',
      name: 'stuIndex',
      component: stuIndex
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/teachingRoom',
      name: 'teachingRoom',
      component: teachingRoom
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/teacher/banStudent',
      name: 'BanStu',
      component: BanStu
    },
    {
      path: '/teacher/timeTable',
      name: 'timeTable',
      component: timeTable
    },
    {
      path: '/teacher/pickTeacher/audit',
      name: 'pickTeacherAudit',
      component: pickTeacherAudit
    }
  ]
})
