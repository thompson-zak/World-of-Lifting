<template>
  <b-container>
    <b-row align-h="center">
      <b-col cols=4></b-col>

      <b-col cols=4>
        <FormKit type="form" name="runningForm" @submit="onSubmit" :actions="false" id="running-form">
          <hr />
          <FormKit
            name="age"
            type="number"
            label="Age"
            validation="required"
          />
          <FormKit
            name="gender"
            type="radio"
            label="Gender"
            :options="['Male', 'Female']"
            value="Male"
            validation="required"
          />
          <FormKit
            name="event"
            type="radio"
            label="Event"
            :options="['5 KM']"
            value="5 KM"
            validation="required"
          />
          <FormKit
            name="time"
            type="time"
            label="Time"
            value="00:00:00"
            validation="required"
          />

          <FormKit
            type="submit"
          />
          <pre wrap>{{ value }}</pre>
        </FormKit>
      </b-col>

      <b-col cols=4></b-col>
    </b-row>
  </b-container>
</template>

<style>
  #running-form {
    background-color: white;
  }
  /* Radio button styling */
  li.formkit-option {
    display: inline-block;
    margin-right: 5px !important;
    margin-left: 5px !important;
  }
</style>

<script>
export default {
  name: 'RunningForm',
  components: {},
  data() {
    return {};
  },
  methods: {},
};
</script>
