<template>
  <div>
    <TeacherFrame :selected="'0'" :title="'房间 '+roomNo+'：直播信息管理'"></TeacherFrame>
    <mu-paper class="paper2" z-depth="4">
      <mu-text-field v-model="value" placeholder="请输入房间简介"></mu-text-field><br/>
      <mu-text-field v-model="value2" placeholder="请输入房间标题"></mu-text-field><br/>
      <mu-flex class="select-control-row">
        <mu-switch v-model="switchVal.value1" label="白板"></mu-switch>
      </mu-flex>
      <mu-flex class="select-control-row">
        <mu-switch v-model="switchVal.value2" label="代码编译区"></mu-switch>
      </mu-flex>
    </mu-paper>
  </div>
</template>

<script>
import TeacherFrame from '../components/TeacherFrame'
import PickStuTabsAccepted from '../components/PickStuTabsAccepted'
import Divider from 'muse-ui/lib'
export default {
  name: 'RoomManage',
  components: {
    Divider,
    TeacherFrame,
    PickStuTabsAccepted
  },
  data () {
    return {
      switchVal: {
        value1: false,
        value2: false
      }
    }
  }
}
</script>

<style scoped>

</style>
