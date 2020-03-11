<template>
  <CollectionView v-if="showType == 'collection'" :playlist="playlist" @play-swf="play"></CollectionView>
  <SwfPlayer v-else :uri="playUri"></SwfPlayer>
</template>

<script>
import CollectionView from "./CollectionView";
import SwfPlayer from "./SwfPlayer";
export default {
  name: "MainView",
  props: ["playlist", "playUri"],
  methods:{
    play:function(index){
      console.log("play item " + index);
      this.playUri = this.playlist[index].uri
    }
  },
  computed: {
    showType: function() {
      if (this.playUri == ''){
        return "collection"
      }else{
        return "swf"
      }
    }
  },
  components: { CollectionView, SwfPlayer}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
