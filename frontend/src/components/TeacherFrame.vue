<template>
  <div id="TeacherFrame">
    <TeacherBar v-bind:title="title"></TeacherBar>
    <TeacherNavigation v-bind:selected="selected"></TeacherNavigation>
  </div>
</template>

<script>
  import TeacherBar from '../components/TeacherBar'
  import TeacherNavigation from '../components/TeacherNavigation'
    export default {
      name: "TeacherFrame",
      components: {
        TeacherBar,
        TeacherNavigation
      },
      props: ['selected','title']
    }
</script>

<style scoped>

</style>
