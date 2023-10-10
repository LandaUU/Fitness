import { useLoaderData } from "react-router-dom";
import { Accordion, AccordionItem, Grid, Column } from "@carbon/react";
import { useEffect } from "react";
import { IceVision, Restaurant, ShapeJoin } from "@carbon/icons-react";
import SingleMeasureCard from "../SingleMeasureCard";
import CaloriesInfo from "../CaloriesInfo";
import FoodDiaryAccordeion from "../FoodDiaryAccordeon/FoodDiaryAccordeon";

const Dashboard = () => {
  const food = useLoaderData();

  useEffect(() => {}, []);

  console.log(food);

  return (
    <Grid>
      <Column lg={4} sm={4} md={4}>
        <CaloriesInfo
          userCaloriesNorm={3500}
          caloriesEated={food?.summary?.calories || 0}
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
            <Column md={8} sm={4} key={key} className={'food-diary-accordion-column'}>
              <FoodDiaryAccordeion food={food.food[key]} mealName={key} className="food-diary-accordeon"/>
            </Column>
          );
        }
      })}
    </Grid>
  );
};

export default Dashboard;
