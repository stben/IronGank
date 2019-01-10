<template>
<div>
<mu-menu placement="top-start" open-on-hover>
    <mu-button color="primary">选择院系</mu-button>
    <mu-list slot="content">
      <mu-list-item button>
        <mu-list-item-title>院系1</mu-list-item-title>
      </mu-list-item>
      <mu-list-item button>
        <mu-list-item-title>院系2</mu-list-item-title>
      </mu-list-item>
      <mu-list-item button>
        <mu-list-item-title>院系3</mu-list-item-title>
      </mu-list-item>
      <mu-list-item button>
        <mu-list-item-title>院系4</mu-list-item-title>
      </mu-list-item>
      <mu-list-item button>
        <mu-list-item-title>院系5</mu-list-item-title>
      </mu-list-item>
    </mu-list>
</mu-menu>
</mu-menu>
<mu-text-field v-model="value" placeholder="请输入房间名称进行搜索"></mu-text-field>
<mu-button color="primary">搜索</mu-button></br>
  <mu-expansion-panel>
    <div slot="header">房间名称1</div>
    房间简介
  </mu-expansion-panel>
  <mu-expansion-panel>
    <div slot="header">房间名称2</div>
   .房间简介
  </mu-expansion-panel>
  <mu-expansion-panel>
    <div slot="header">房间名称3</div>
    房间简介
  </mu-expansion-panel>
</div>
</template>

<script>
export default {
  data () {
    return {
      value: '',
      visibility: false
    }
  }
}
</script>

<style scoped>
.button-wrapper {
  text-align: center;
  .mu-button{
    margin: 8px;
  }
}
</style>
