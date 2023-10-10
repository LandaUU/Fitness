import { Layer, Grid, Column } from "@carbon/react";
import PropTypes from "prop-types";

const CaloriesInfo = ({ userCaloriesNorm, caloriesEated }) => {
  return (
    <Layer className="calories-info">
      <Grid>
        <Column sm={4}>
          <h1 className="calories-percent">
            {Math.floor((caloriesEated / userCaloriesNorm) * 100)} %
          </h1>
        </Column>
        <Column sm={2}>
          <p className="calories-remained">
            Осталось: {Math.floor(userCaloriesNorm - caloriesEated)} Ккал
          </p>
        </Column>
        <Column sm={2}>
          <p className="calories-eaten">Употреблено: {caloriesEated} Ккал</p>
        </Column>
      </Grid>
    </Layer>
  );
};

CaloriesInfo.propTypes = {
  userCaloriesNorm: PropTypes.number,
  caloriesEated: PropTypes.number,
};

export default CaloriesInfo;
