<template>
  <h2>Powerlifting Analysis</h2>

  <br>

  <b-container>
    <b-row align-h="center">
      <b-col cols=3></b-col>

      <b-col cols=6>

        <FormKit type="form" :actions="false">
          <FormKit type="multi-step" tab-style="progress">
            <FormKit type="step" name="lifts">
              <FormKit
                  id="squat"
                  type="number"
                  label="Squat"
                  validation="required"
              />
              <FormKit
                id="bench"
                type="number"
                label="Bench"
                validation="required"
              />
              <FormKit
                id="deadlift"
                type="number"
                label="Deadlift"
                validation="required"
              />
              <FormKit
                id="liftUnits"
                type="radio"
                label="Units"
                :options="['lbs', 'kg']"
                validation="required"
              />
            </FormKit>

            <FormKit type="step" name="liftClass">
              <FormKit
                  id="equipped"
                  type="radio"
                  label="Equipped?"
                  :options="['Equipped', 'Raw']"
                  validation="required"
              />
              <FormKit
                id="bodyweight"
                type="number"
                label="Bodyweight"
                validation="required"
              />
              <FormKit
                id="bodyweightUnits"
                type="radio"
                label="Units"
                :options="['lbs', 'kg']"
                validation="required"
              />
            </FormKit>

            <FormKit type="step" name="demographics">
              <FormKit
                  id="age"
                  type="number"
                  label="Age"
                  validation="required"
              />
              <FormKit
                id="gender"
                type="radio"
                label="Gender"
                :options="['Male', 'Female', 'Non-Binary']"
                validation="required"
              />

              <!-- using step slot for submit button-->
              <template #stepNext>
                <FormKit type="submit" />
              </template>
            </FormKit>
          </FormKit>
        </FormKit>
      </b-col>

      <b-col cols=3></b-col>
    </b-row>
  </b-container>
</template>

<style>
  .formkit-steps {
    background-color: white;
  }
</style>

<script>
// import axios from 'axios';

export default {
  name: 'PowerliftingForm',
  data() {
    return {};
  },
  methods: {
    onSubmit(formData, node) {
      /* event.preventDefault();
      this.$emit('requestSubmitted', true);

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

      axios.post(path, requestBody)
        .then((res) => {
          this.$emit('analyzeLiftsData', res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          // TODO - update error handling
          console.error(error);
        });

      this.show = true; */
      console.log(formData);
      console.log(node);
    },
  },
};
</script>
