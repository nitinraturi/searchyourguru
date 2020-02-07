<template>
  <form action="#" v-on:submit.prevent="search" method="get">
    <div class="columns is-multiline">
      <div class="column is-3">
        <!-- City  -->
        <div class="field is-horizontal">
          <div class="field-body">
            <div class="field">
              <label class="label">City | Pincode</label>
              <div class="control">
                <input
                  type="text"
                  class="input"
                  placeholder="eg: Delhi or 110092"
                  v-model="location_keyword"
                  required
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="column is-3">
        <!-- City  -->
        <div class="field is-horizontal">
          <div class="field-body">
            <div class="field">
              <label class="label">Looking For</label>
              <div class="control">
                <select name="type" class="input" v-model="user_type">
                  <option value="4">Tutors</option>
                  <option value="3">Students</option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="column is-3">
        <!-- City  -->
        <div class="field is-horizontal">
          <div class="field-body">
            <div class="field">
              <label class="label">Course</label>
              <div class="control">
                <input
                  type="text"
                  class="input"
                  placeholder="eg:Math"
                  v-model="category"
                  required
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="column is-3">
        <div class="field">
          <label for="" class="label">
            <span class="icon is-small is-left">
              <i class="fas fa-search"></i>
            </span>
          </label>
          <p class="control">
            <button
              type="submit"
              v-on:submit.prevent="search"
              class="button is-success"
            >
              Search
            </button>
          </p>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  name: 'FilterForm',
  data: function() {
    return {
      location_keyword: '',
      user_type: 4,
      category: ''
    }
  },
  methods: {
    search: function() {
      this.$router.push('/search/')
    }
  }
}
</script>

<style></style>
