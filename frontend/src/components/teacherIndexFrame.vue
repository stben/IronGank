<template>
  <div id="TeacherFrame">
    <TeacherBar v-bind:title="title"></TeacherBar>
    <teacherIndexNavigation v-bind:selected="selected"></teacherIndexNavigation>
  </div>
</template>

<script>
import TeacherBar from '../components/TeacherBar'
import teacherIndexNavigation from '../components/teacherIndexNavigation'
export default {
  name: 'TeacherFrame',
  components: {
    TeacherBar,
    teacherIndexNavigation
  },
  props: ['selected', 'title']
}
</script>

<style scoped>

</style>
