import Vue from 'vue'
import Router from 'vue-router'
import roomManage from '@/components/roomManage'
import teacherIndex from '@/components/teacherIndex'
import pickStudentAudit from '@/components/pickStudentAudit'
import pickStudentAccepted from '@/components/pickStudentAccepted'
import studentIndex from '@/components/studentIndex'
import teachingRoom from '@/components/teachingRoom'
import login from '@/components/login'
import banStudent from '@/components/banStudent'
import timeTable from '@/components/timeTable'
import register from '@/components/register'
import pickTeacherAudit from '@/components/pickTeacherAudit'
import pickTeacherAccepted from '@/components/pickTeacherAccepted'
import teacherLogin from '@/components/teacherLogin'
import studentLogin from '@/components/studentLogin'
import stuStudyRoom from '@/components/stuStudyRoom'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/teacher/index',
      name: 'teacherIndex',
      component: teacherIndex
    },
    // {
    //   path: '/',
    //   name: 'login',
    //   component: login
    // },
    {
      path: '/teacher/roomManage',
      name: 'roomManage',
      component: roomManage
    },
    {
      path: '/teacher/pickStudent/audit',
      name: 'pickStudentAudit',
      component: pickStudentAudit
    },
    {
      path: '/teacher/pickStudent/accepted',
      name: 'pickStudentAccepted',
      component: pickStudentAccepted
    },
    {
      path: '/student/index',
      name: 'studentIndex',
      component: studentIndex
    },
    {
      path: '/student/studyRoom',
      name: 'studentStudyRoom',
      component: stuStudyRoom
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/teacher/teachingRoom',
      name: 'teachingRoom',
      component: teachingRoom
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/teacher/banStudent',
      name: 'banStudent',
      component: banStudent
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
    },
    {
      path: '/teacher/pickTeacher/accepted',
      name: 'pickTeacherAccepted',
      component: pickTeacherAccepted
    },
    {
      path: '/teacher/login',
      name: 'teacherLogin',
      component: teacherLogin
    },
    {
      path: '/student/login',
      name: 'studentLogin',
      component: studentLogin
    }
  ]
})
