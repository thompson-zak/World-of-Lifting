<template>
  <b-card>
    <div class="container">
      <div>

        <h1>Compare Your Lifts!</h1>

        <hr><br><br>

        <b-form @submit="onSubmit">
          <b-form-group
            id="squat-group"
            label="Squat:"
            label-for="squat-input"
          >
            <b-form-input
              id="squat-input"
              v-model="form.squat"
              type="number"
              placeholder="Enter squat here"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="bench-group"
            label="Bench:"
            label-for="bench-input"
          >
            <b-form-input
              id="bench-input"
              v-model="form.bench"
              type="number"
              placeholder="Enter bench press here"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="deadlift-group"
            label="Deadlift:"
            label-for="deadlift-input"
          >
            <b-form-input
              id="deadlift-input"
              v-model="form.deadlift"
              type="number"
              placeholder="Enter deadlift here"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="lift-units-group">
            <b-form-checkbox-group
              v-model="form.liftUnits"
              id="lift-units-checkbox"
            >
              <b-form-checkbox value="lbs">lbs</b-form-checkbox>
              <b-form-checkbox value="kgs">kgs</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-form-group
            id="age-group"
            label="Age:"
            label-for="age-input"
          >
            <b-form-input
              id="age-input"
              v-model="form.age"
              type="number"
              placeholder="Enter age here"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="bodyweight-group"
            label="Bodyweight:"
            label-for="bodyweight-input"
          >
            <b-form-input
              id="bodyweight-input"
              v-model="form.bodyweight"
              type="number"
              placeholder="Enter bodyweight here"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="bodyweight-units-group">
            <b-form-checkbox-group
              v-model="form.bodyweightUnits"
              id="bodyweight-units-checkbox"
            >
              <b-form-checkbox value="lbs">lbs</b-form-checkbox>
              <b-form-checkbox value="kgs">kgs</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>

        <hr><br><br>

        <b-card class="mt-3" header="Form Data Result" v-if="show">
          <pre class="m-0">{{ result }}</pre>
      </b-card>
      </div>
    </div>
  </b-card>
</template>

<script>
export default {
  data() {
    return {
      form: {
        squat: 0,
        bench: 0,
        deadlift: 0,
        liftUnits: 'lbs',
        age: 0,
        bodyweight: 0,
        bodyweightUnits: 'lbs',
      },
      show: false,
      result: null,
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      this.show = true;
      this.result = JSON.stringify(this.form);
    },
  },
};
</script>
