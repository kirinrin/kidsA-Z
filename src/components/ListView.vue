<template>
  <el-aside width="150px">
    <el-menu default-active="0">
      <el-menu-item
        :index="index.toString()"
        :key="item.name"
        v-for="(item, index) in playlist"
        @click="$emit('chnage-item',index)"
      >
        <i class="el-icon-folder"></i>
        {{item.name}}
      </el-menu-item>
    </el-menu>
  </el-aside>
</template>

<script>
export default {
  name: "ListView",
  props: ["playlist"]
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
