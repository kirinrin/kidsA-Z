<template>
  <el-main>
    <div
      style="flex-wrap: wrap; display: flex; display: -webkit-flex; /* Safari */; align-content: flex-start;"
    >
      <el-card
        shadow="hover"
        :index="index.toString()"
        :key="item.name"
        v-for="(item, index) in playlist"
        body-style="background-color: aliceblue;width: 200px;
  height: 200px; padding: 0px; cursor: pointer;" style="margin: 5px;"
      >
        <el-image :src="defaultSrc" v-on:click="playItem(index)">
          <div slot="placeholder">
          </div>
        </el-image>
        <div style="padding: 14px;" v-on:click="playItem(index)">
        <span>{{item.name}}</span>
      </div>
      </el-card>
    </div>
  </el-main>
</template>

<script>
export default {
  data: function() {
    return {
      defaultSrc:
        "https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg"
    };
  },
  name: "CollectionView",
  props: ["playlist"],
  methods: {
    playItem: function(index) {
      this.$emit('play-swf',index);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.swf-card {
  margin: 5px;
  width: 200px;
  height: 200px;
  cursor: pointer;
  background-color: aliceblue;
  padding: 0px;
}
.image-slot {
  padding: 0px;
}
</style>
