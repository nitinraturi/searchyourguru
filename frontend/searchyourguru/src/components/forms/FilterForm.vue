<template>
  <form action="#" method="get">
    <div class="columns is-multiline">
      <div class="column is-3">
        <!-- City  -->
        <div class="field is-horizontal">
          <div class="field-body">
            <div class="field">
              <label class="label">City</label>
              <div class="control">
                <select name="city" class="input">
                  <option value="0">Delhi</option>
                  <option value="0">Delhi</option>
                  <option value="0">Delhi</option>
                  <option value="0">Delhi</option>
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
              <label class="label">Looking</label>
              <div class="control">
                <select name="type" class="input">
                  <option value="0">Tutors</option>
                  <option value="0">Students</option>
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
                <select name="type" class="input">
                  <option value="0">BCA</option>
                  <option value="0">MCA</option>
                </select>
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
            <button type="submit" class="button is-success">
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
  name: 'FilterForm'
}
</script>

<style></style>
