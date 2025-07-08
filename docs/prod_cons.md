This Excel file provides time-dependent data for both **generation** and **consumption** associated with the elements in the network. Each sheet represents a dataset related to specific elements such as generators or loads, and includes detailed profiles for power production, consumption, and availability.

This page explains how the data should be organized, the required fields for each sheet, and best practices for preparing consistent and accurate input.
It's defined by a `.xlsx` file named after the case, for example, `case9.xlsx`.

This file is divided into 5 sheets.

#### **Structure Breakdown**:

| Sheet name | Data Type | Explanation                                                                              |
|:----------:|:---------:|:-----------------------------------------------------------------------------------------|
|     Pc     |   float   | Value of **active power consumption** of each load (lines) in each period (columns)      |
|     Qc     |   float   | Value of **reactive power consumption** of each load (lines) in each period (columns)    |
|   UpFlex   |   float   | Value of **upward flexibility** of each load (lines) in each period (columns)            |
|  DownFlex  |   float   | Value of **downward flexibility** of each load (lines) in each period (columns)          |
|     Pg     |   float   | Value of **active power generated** of each generator (lines) in each period (columns)   |
|     Qg     |   float   | Value of **reactive power generated** of each generator (lines) in each period (columns) |
| GenStatus  |  integer  | Status of each generator (lines) in each period (columns); 1 - Online, 0 - Offline       |
