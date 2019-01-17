<template>
  <div id="pickTeacherAccepted">
    <teacherFrame :selected="'3'" :title="'房间 '+roomNo+'：助教列表'" :roomNo="roomNo"></teacherFrame>
    <pickTeacherTabsAccepted v-bind:acceptedList="acceptedList" :roomNo="roomNo"></pickTeacherTabsAccepted>
  </div>
</template>

<script>
import teacherFrame from './teacherFrame'
import pickTeacherTabsAccepted from '../components/pickTeacherTabsAccepted'
export default {
  name: 'pickTeacherAccepted',
  components: {
    teacherFrame,
    pickTeacherTabsAccepted
  },
  data() {
    return {
      roomNo: this.$route.params.roomNo,
      acceptedList: []
    }
  },
  mounted () {
    this.getPickTeachers()
  },
  methods: {
    getPickTeachers() {
      this.$axios.request({
        url: '/api/teacher/pickTeacher',
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
