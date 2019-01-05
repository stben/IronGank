import Vue from 'vue'
import Router from 'vue-router'
import RoomManage from '@/components/RoomMange'
import TeacherIndex from '@/components/TeacherIndex'
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
    }
  ]
})
