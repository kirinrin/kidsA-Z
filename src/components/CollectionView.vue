<template>
  <el-main>
    <div
      style="flex-wrap: wrap; display: flex; display: -webkit-flex; /* Safari */; align-content: flex-start;"
    >
      <div
        :index="index.toString()"
        :key="item.name"
        v-for="(item, index) in playlist"
        style="margin: 5px; width: 200px; height: 200px; background-color: #67c23a"
        v-on:click="playItem(index)"
      >{{index}} = {{item.name}}</div>
    </div>
  </el-main>
</template>

<script>
export default {
  name: "CollectionView",
  props: ["playlist"],
  methods: {
    playItem: function(index) {
      console.log("play item " + index);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
