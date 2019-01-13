<template>
    <div>
        <stuFrame :selected="''" :title="'学生 '+stuNo+''"></stuFrame>
    </div>
</template>

<script>
import stuFrame from '../components/stuFrame'
export default {
  name: 'teachingRoom',
  components: {
    stuFrame
  }
}
</script>

<style scoped>

</style>
