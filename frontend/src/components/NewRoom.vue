<template xmlns="http://www.w3.org/1999/html">
  <div>
    <TeacherFrame :selected="'4'" :title="'新建房间'"></TeacherFrame>
    <mu-paper class="paper3" z-depth="4">
      <mu-text-field v-model="value" placeholder="请输入房间名称"></mu-text-field><br/>
      <mu-text-field v-model="value2" placeholder="请输入房间标题"></mu-text-field><br/>
      <mu-flex class="select-control-row">
        <mu-switch v-model="switchVal.value1" label="白板"></mu-switch>
      </mu-flex>
      <mu-flex class="select-control-row">
        <mu-switch v-model="switchVal.value2" label="代码编译区"></mu-switch>
      </mu-flex>
      <mu-text-field v-model="value3" placeholder="房间简介" multi-line :rows="3" :rows-max="6">
      </mu-text-field><br/>
      <mu-button color="primary">确认创建房间</mu-button>
    </mu-paper>
  </div>
</template>

<script>
import TeacherFrame from '../components/TeacherFrame'
import PickStuTabsAccepted from '../components/PickStuTabsAccepted'
import Divider from 'muse-ui/lib'
export default {
  name: 'NewRoom',
  components: {
    Divider,
    TeacherFrame,
    PickStuTabsAccepted
  },
  data () {
    return {
      switchVal: {
        value1: false,
        value2: false,
        value3: ''
      }
    }
  }
}
</script>

<style scoped>
.paper3{
    margin: -200px 300px;
  }
</style>
