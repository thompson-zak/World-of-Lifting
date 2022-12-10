<template>
  <b-card>
    <div class="container">
      <div>

        <h1>Compare Your Lifts!</h1>

        <hr><br><br>

        <b-form @submit="onSubmit" @reset="onReset">
          <b-form-group
            id="squat-group"
            label="Squat:"
            label-for="squat-input"
          >
            <b-form-input
              id="squat-input"
              v-model="form.squat"
              type="text"
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
              type="text"
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
              type="text"
              placeholder="Enter deadlift here"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="lift-units-group">
            <b-form-radio-group
              id="lift-units-radio"
              v-model="selectedLiftUnits"
              :options="liftOptions"
            ></b-form-radio-group>
          </b-form-group>

          <br>

          <b-form-group
            id="age-group"
            label="Age:"
            label-for="age-input"
          >
            <b-form-input
              id="age-input"
              v-model="form.age"
              type="text"
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
              type="text"
              placeholder="Enter bodyweight here"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="bodyweight-units-group">
            <b-form-radio-group
              id="bodyweight-units-radio"
              v-model="selectedBodyweightUnits"
              :options="bodyweightOptions"
            ></b-form-radio-group>
          </b-form-group>

          <br>

          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
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
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        squat: null,
        bench: null,
        deadlift: null,
        liftUnits: 'lbs',
        age: null,
        bodyweight: null,
        bodyweightUnits: 'lbs',
      },
      show: false,
      result: null,
      selectedLiftUnits: 'lbs',
      liftOptions: [
        { text: 'Pounds', value: 'lbs' },
        { text: 'Kilos', value: 'kgs' },
      ],
      selectedBodyweightUnits: 'lbs',
      bodyweightOptions: [
        { text: 'Pounds', value: 'lbs' },
        { text: 'Kilos', value: 'kgs' },
      ],
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();

      const path = 'http://localhost:5000/analyze-lifts';
      const requestBody = {
        squat: Number(this.form.squat),
        bench: Number(this.form.bench),
        deadlift: Number(this.form.deadlift),
        liftUnits: this.form.liftUnits,
        age: Number(this.form.age),
        bodyweight: Number(this.form.bodyweight),
        bodyweightUnits: this.form.bodyweightUnits,
      };
      console.log(requestBody);
      axios.post(path, requestBody)
        .then((res) => {
          this.result = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });

      this.show = true;
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.result = null;
      this.show = false;
    },
  },
};
</script>
