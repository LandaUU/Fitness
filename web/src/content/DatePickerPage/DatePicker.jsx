import { useEffect, useState } from "react";
import { Button, DatePicker, DatePickerInput, Layer } from "@carbon/react";

const DatePickerPage = () => {
  const [date, setDate] = useState(null);

  useEffect(() => {
    window.Telegram.WebApp.ready();
    console.log(`initData = ${window.Telegram.WebApp.initData}`);
  }, []);

  return (
    <Layer className="date-picker-container">
      <div className="date-picker-subcontainer">
        <DatePicker
          className="date-picker-report"
          datePickerType="single"
          value={date}
          onChange={(value) => {
            setDate(value[0]);
          }}
        >
          <DatePickerInput
            className="date-picker-input-report"
            placeholder="ММ/ДД/ГГГГ"
            labelText="Выберите дату для выгрузки отчета"
            size="md"
          />
        </DatePicker>
      </div>
      <div className="date-picker-subcontainer">
        <Button
          className="date-picker-submit"
          onClick={() => {
            if (date) {
              const offset = date.getTimezoneOffset();
              const strDate = new Date(date.getTime() - offset * 60 * 1000)
                .toISOString()
                .split("T")[0];
              window.Telegram.WebApp.sendData(strDate);
            }
          }}
        >
          Выбрать
        </Button>
      </div>
    </Layer>
  );
};

export default DatePickerPage;
