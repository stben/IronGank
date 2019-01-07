import Vue from 'vue'
import Router from 'vue-router'
import PickStuAudit from '@/components/PickStuAudit'
import PickStuAccepted from '@/components/PickStuAccepted'
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
  ]
})
