<template>
  <CollectionView v-if="showType == 'collection'" :playlist="playlist" ></CollectionView>
  <SwfPlayer v-else :uri="playlist.uri"></SwfPlayer>
</template>

<script>
import CollectionView from "./CollectionView";
import SwfPlayer from "./SwfPlayer";
export default {
  name: "MainView",
  props: ["playlist"],
  computed: {
    showType: function() {
      var data = this.playlist;
      if (data.sub == undefined) {
        return "collection";
      } else {
        console.log("show swf player");
        return "swf";
      }
    }
  },
  components: { CollectionView, SwfPlayer}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
