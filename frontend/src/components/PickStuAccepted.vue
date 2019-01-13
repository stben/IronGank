<template>
  <div id="PickStuAccepted">
    <TeacherFrame :selected="'1'" :title="'房间 '+roomNo+'：可排队学生列表'"></TeacherFrame>
    <PickStuTabsAccepted v-bind:acceptedList="acceptedList"></PickStuTabsAccepted>
  </div>
</template>

<script>
import TeacherFrame from '../components/TeacherFrame'
import PickStuTabsAccepted from '../components/PickStuTabsAccepted'
export default {
  name: 'PickStuAccepted',
  components: {
    TeacherFrame,
    PickStuTabsAccepted
  },
  data() {
    return {
      roomNo: 30150, // 要把房间号改了
      acceptedList: [
        { stuName: '赵六', stuNo: '20162853' }, { stuName: '钱七', stuNo: '20162971' }, { stuName: '孙八', stuNo: '20162142' },
        { stuName: '杨九', stuNo: '20162031' }, { stuName: '吴十', stuNo: '20162672' }
      ]
    }
  }
}
</script>

<style scoped>

</style>
