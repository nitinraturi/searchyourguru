<template>
  <div class="modal" v-bind:class="{ 'is-active': show == true }">
    <div class="modal-background"></div>
    <div class="modal-content" style="overflow:hidden">
      <center>
        <!-- <div class="loader"></div> -->
        <!-- <p class="has-text-white">Loading SYG</p> -->
        <button
          class="button is-small is-link is-outlined is-rounded is-loading"
        >
          Loading
        </button>
      </center>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'loading-bar',

  data() {
    return {
      show: false
    }
  },

  computed: {
    ...mapGetters(['getLoading'])
  },

  methods: {
    showProgress(show) {
      this.show = show
    },
    start() {
      this.show = true
    },
    stop() {
      this.show = false
    }
  },

  watch: {
    getLoading: function(val) {
      console.log(val)
      if (val) {
        this.start()
      } else {
        this.stop()
      }
    }
  }
}
</script>
