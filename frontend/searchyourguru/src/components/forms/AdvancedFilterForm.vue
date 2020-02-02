<template>
  <div>
    <form action="#">
      <div class="field">
        <label for="" class="subtitle is-size-6 has-text-success"
          >City / Pincode</label
        >
        <div class="control">
          <input type="text" placeholder="" class="input is-small" />
        </div>
      </div>

      <div class="field">
        <label for="#" class="subtile is-6 has-text-success">Course</label>
        <div class="control">
          <select name="" id="" class="input">
            <option value="0">Bca</option>
            <option value="0">Bca</option>
          </select>
        </div>
      </div>

      <div class="field">
        <label for="#" class="subtile is-6 has-text-success">Subject</label>
        <div class="control">
          <select name="" id="" class="input">
            <option value="0">Math</option>
            <option value="0">English</option>
          </select>
        </div>
      </div>

      <div class="field">
        <label for="#" class="subtile is-6 has-text-success">Gender</label>
        <div class="control">
          <select name="" id="" class="input">
            <option value="0">Male</option>
            <option value="0">Female</option>
          </select>
        </div>
      </div>

      <div class="field">
        <label for="#" class="subtile is-6 has-text-success">Experience</label>
        <div class="control">
          <select name="" id="" class="input">
            <option value="0">0 -2 Years</option>
            <option value="0">2 -5 Years</option>
          </select>
        </div>
      </div>

      <div class="field">
        <label for="#" class="subtile is-6 has-text-success"
          >Per Hour Fees</label
        >
        <div class="control">
          <select name="" id="" class="input">
            <option value="0">Upto Rs 200</option>
            <option value="0">Rs 201 - Rs 500</option>
          </select>
        </div>
      </div>

      <div class="field is-grouped-centered is-grouped">
        <p class="control">
          <button type="submit" class="button is-success">
            Apply
          </button>
        </p>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AdvancedFilterForm'
}
</script>

<style></style>
