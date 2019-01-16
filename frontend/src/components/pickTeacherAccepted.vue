<template>
  <div id="pickTeacherAccepted">
    <TeacherFrame :selected="'3'" :title="'房间 '+roomNo+'：助教列表'" :roomNo="roomNo"></TeacherFrame>
    <pickTeacherTabsAccepted v-bind:acceptedList="acceptedList" :roomNo="roomNo"></pickTeacherTabsAccepted>
  </div>
</template>

<script>
import TeacherFrame from '../components/TeacherFrame'
import pickTeacherTabsAccepted from '../components/pickTeacherTabsAccepted'
export default {
  name: 'pickTeacherAccepted',
  components: {
    TeacherFrame,
    pickTeacherTabsAccepted
  },
  data() {
    return {
      roomNo: this.$route.params.roomNo,
      acceptedList: []
    }
  },
  mounted () {
    this.getPickStudents()
  },
  methods: {
    getPickStudents() {
      this.$axios.request({
        url: '/api/teacher/pickStudent',
        params: {
          'roomNo': this.$route.params.roomNo
        },
        method: 'get'
      }).then((response) => {
        this.acceptedList = response.data.acceptedList
      })
    }
  }
}
</script>

<style scoped>

</style>
