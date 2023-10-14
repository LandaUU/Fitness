import { useLoaderData } from "react-router-dom";
import { Grid, Column } from "@carbon/react";
import { useEffect } from "react";
import { IceVision, ShapeJoin } from "@carbon/icons-react";
import SingleMeasureCard from "../SingleMeasureCard";
import CaloriesInfo from "../CaloriesInfo";
import FoodDiaryAccordion from "../FoodDiaryAccordion/FoodDiaryAccordion";
import NutriensPie from "../NutrientsPie";

const Dashboard = () => {
  const food = useLoaderData();

  useEffect(() => {}, []);

  return (
    <Grid className="dashboard-grid">
      <Column lg={4} sm={4} md={4}>
        <CaloriesInfo
          userCaloriesNorm={6500}
          caloriesEated={food.food?.summary?.calories || 0}
        />
      </Column>
      <Column md={2} sm={2} lg={4} className="user-weight-column">
        <SingleMeasureCard Icon={IceVision} name={"Вес"} value={food.weight} />
      </Column>
      <Column md={2} sm={2} lg={4} className="user-steps-column">
        <SingleMeasureCard Icon={ShapeJoin} name={"Шаги"} value={food.steps} />
      </Column>
      {Object.keys(food.food).map((key) => {
        if (key !== "summary") {
          return (
            <Column
              md={8}
              sm={4}
              key={key}
              className={"food-diary-accordion-column"}
            >
              <FoodDiaryAccordion
                food={food.food[key]}
                mealName={key}
                className="food-diary-accordeon"
              />
            </Column>
          );
        }
      })}
      <Column lg={16} md={8} sm={4}>
        <NutriensPie foodSummary={food.food.summary} />
      </Column>
    </Grid>
  );
};

export default Dashboard;
