import { Layer } from "@carbon/react";
import PropTypes from "prop-types";

const SingleMeasureCard = ({ name, value, Icon }) => {
  return (
    <Layer className={"single-measure-card-layer"}>
      <div className="single-measure-card">
        <Icon />
        <div>{name}</div>
        <div>{value}</div>
      </div>
    </Layer>
  );
};

SingleMeasureCard.propTypes = {
  name: PropTypes.string,
  value: PropTypes.number,
  Icon: PropTypes.element,
};

export default SingleMeasureCard;
