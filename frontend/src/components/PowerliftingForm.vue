<template>
    <b-card>
        <div class="container">
            <div>
                <br>
                <b-form @submit="onSubmit" @reset="onReset">

                  <b-form-row>
                    <b-col cols="3"></b-col>
                    <b-col cols="2">
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
                    </b-col>

                    <b-col cols="2">
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
                    </b-col>

                    <b-col cols="2">
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
                    </b-col>
                    <b-col cols="3"></b-col>
                  </b-form-row>

                  <b-form-group id="lift-units-group">
                    <b-form-radio-group
                      id="lift-units-radio"
                      v-model="selectedLiftUnits"
                      :options="liftOptions"
                    ></b-form-radio-group>
                  </b-form-group>

                  <br>

                  <b-form-row>
                    <b-col cols="5"></b-col>
                    <b-col cols="2">
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
                    </b-col>
                    <b-col cols="5"></b-col>
                  </b-form-row>

                  <br>

                  <b-form-row>
                    <b-col cols="5"></b-col>
                    <b-col cols="2">
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
                    </b-col>
                    <b-col cols="5"></b-col>
                  </b-form-row>

                  <b-form-group id="bodyweight-units-group">
                    <b-form-radio-group
                      id="bodyweight-units-radio"
                      v-model="selectedBodyweightUnits"
                      :options="bodyweightOptions"
                    ></b-form-radio-group>
                  </b-form-group>

                  <br>

                  <b-form-row>
                    <b-col cols="3"></b-col>
                    <b-col cols="3">
                      <b-form-group id="sex-group" label="Gender?">
                        <b-form-radio-group
                          id="sex-radio"
                          v-model="selectedSex"
                          :options="sexOptions"
                        ></b-form-radio-group>
                      </b-form-group>
                    </b-col>

                    <b-col cols="3">
                      <b-form-group id="equipped-group" label="Raw or Equipped?">
                        <b-form-radio-group
                          id="equipped-radio"
                          v-model="selectedEquipped"
                          :options="equippedOptions"
                        ></b-form-radio-group>
                      </b-form-group>
                    </b-col>
                    <b-col cols="3"></b-col>
                  </b-form-row>

                  <br>

                  <b-button type="submit" variant="primary">Submit</b-button>
                  <b-button type="reset" variant="danger">Reset</b-button>
                </b-form>
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
        sex: 'M',
        equipped: 'equipped',
      },
      show: false,
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
      selectedSex: 'M',
      sexOptions: [
        { text: 'Male', value: 'M' },
        { text: 'Female', value: 'F' },
        { text: 'Non-Binary', value: 'Mx' },
      ],
      selectedEquipped: 'raw',
      equippedOptions: [
        { text: 'Raw', value: 'raw' },
        { text: 'Equipped', value: 'equipped' },
      ],
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();

      const path = 'http://localhost:5000/analyze-lifts';
      const equippedBool = this.form.equipped === 'equipped';
      const requestBody = {
        squat: Number(this.form.squat),
        bench: Number(this.form.bench),
        deadlift: Number(this.form.deadlift),
        liftUnits: this.form.liftUnits,
        age: Number(this.form.age),
        bodyweight: Number(this.form.bodyweight),
        bodyweightUnits: this.form.bodyweightUnits,
        sex: this.form.sex,
        equipped: equippedBool,
      };
      console.log(requestBody);
      axios.post(path, requestBody)
        .then((res) => {
          this.$emit('analyzeLiftsData', res.data);
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
      this.show = false;
    },
  },
};
</script>
