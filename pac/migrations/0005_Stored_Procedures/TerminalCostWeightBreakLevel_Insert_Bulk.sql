﻿CREATE OR ALTER PROCEDURE [dbo].[TerminalCostWeightBreakLevel_Insert_Bulk]
	@TerminalCostWeightBreakLevelTableType CostWeightBreakLevelTableType READONLY,
	@UpdatedBy nvarchar(50) = NULL,
	@Comments nvarchar(4000) = NULL
AS

SET NOCOUNT ON;

DECLARE @ERROR1 INT, @ERROR2 INT, @ROWCOUNT1 INT, @ROWCOUNT2 INT, @InputCount INT;

SELECT @InputCount = Count(*) FROM @TerminalCostWeightBreakLevelTableType;

IF @UpdatedBy IS NULL
	SELECT @UpdatedBy = 'P&C System';

IF @Comments IS NULL
	SELECT @Comments = 'Created first version.';

BEGIN TRAN

DECLARE @TerminalCostWeightBreakLevel table 
( 
    [WeightBreakLevelID]    BIGINT       NOT NULL,
    [WeightBreakLevelName]  NVARCHAR (50) NOT NULL,
    [WeightBreakLowerBound] INT           NOT NULL,
    [ServiceOfferingID]     BIGINT        NOT NULL
)

DECLARE @TerminalCostWeightBreakLevelID table 
( 
    [WeightBreakLevelName]  NVARCHAR (50) NOT NULL,
    [WeightBreakLowerBound] INT           NOT NULL,
    [ServiceOfferingID]     BIGINT        NOT NULL
)

DECLARE @ServiceOfferingVersionID table 
( 
	[ServiceOfferingID] [bigint] NOT NULL,
	[ServiceOfferingVersionID] [bigint] NOT NULL
)

INSERT INTO @TerminalCostWeightBreakLevelID
(
    [WeightBreakLevelName],
    [WeightBreakLowerBound],
    [ServiceOfferingID]
)
SELECT WB.[WeightBreakLevelName],
    WB.[WeightBreakLowerBound],
    SO.[ServiceOfferingID]
FROM @TerminalCostWeightBreakLevelTableType WB
INNER JOIN dbo.[ServiceOffering] SO ON WB.[ServiceOfferingName] = SO.[ServiceOfferingName]


INSERT INTO @ServiceOfferingVersionID
(
	[ServiceOfferingID],
	[ServiceOfferingVersionID]
)
SELECT [ServiceOfferingID],
	[ServiceOfferingVersionID]
FROM [dbo].[ServiceOffering_History] SLH
WHERE SLH.[IsLatestVersion] = 1
AND [ServiceOfferingID] IN (SELECT DISTINCT [ServiceOfferingID] FROM @TerminalCostWeightBreakLevelID)


INSERT INTO [dbo].[TerminalCostWeightBreakLevel]
(
    [WeightBreakLevelName],
    [WeightBreakLowerBound],
    [ServiceOfferingID],
	[IsActive],
	[IsInactiveViewable]
)
OUTPUT INSERTED.[WeightBreakLevelID],
	 INSERTED.[WeightBreakLevelName],
	 INSERTED.[WeightBreakLowerBound],
	 INSERTED.[ServiceOfferingID]
INTO @TerminalCostWeightBreakLevel
(
	[WeightBreakLevelID],
    [WeightBreakLevelName],
    [WeightBreakLowerBound],
    [ServiceOfferingID]
)
SELECT [WeightBreakLevelName],
    [WeightBreakLowerBound],
    [ServiceOfferingID],
	1,
	1
FROM @TerminalCostWeightBreakLevelID 

SELECT @ERROR1 = @@ERROR, @ROWCOUNT1 = @@ROWCOUNT  

INSERT INTO [dbo].[TerminalCostWeightBreakLevel_History]
(
	[WeightBreakLevelID],
	[WeightBreakLevelName],
    [WeightBreakLowerBound],
    [ServiceOfferingVersionID],
	[IsActive],
	[VersionNum],
	[IsLatestVersion],
	[IsInactiveViewable],
	[UpdatedOn],
	[UpdatedBy],
	[Comments]
)
SELECT WB.[WeightBreakLevelID],
	WB.[WeightBreakLevelName],
    WB.[WeightBreakLowerBound],
    SO.[ServiceOfferingVersionID],
	 1,
	 1,
	 1,
	 1,
	 GETUTCDATE(),
	 @UpdatedBy,
	 @Comments
FROM @TerminalCostWeightBreakLevel WB 
INNER JOIN @ServiceOfferingVersionID SO ON WB.[ServiceOfferingID] = SO.[ServiceOfferingID]

SELECT @ERROR2 = @@ERROR, @ROWCOUNT2 = @@ROWCOUNT 

IF (@ERROR1 <> 0) OR (@ERROR2 <> 0)

	BEGIN
	ROLLBACK TRAN
	RAISERROR('Insert Procedure Failed!', 16, 1)
	RETURN 0
	END

IF (@ROWCOUNT1 <> @InputCount) OR (@ROWCOUNT2 <> @InputCount)
	
	BEGIN
	ROLLBACK TRAN
	IF (@ROWCOUNT1 <> @InputCount)
		RAISERROR('%d Records Affected by Insert Procedure while the expected number of record is %d!', 16, 1, @ROWCOUNT1,  @InputCount);
	IF (@ROWCOUNT2 <> @InputCount)
		RAISERROR('%d Records Affected by Insert Procedure while the expected number of record is %d!', 16, 1, @ROWCOUNT2, @InputCount);
	RETURN 0
	END

COMMIT TRAN

RETURN 1

GO
