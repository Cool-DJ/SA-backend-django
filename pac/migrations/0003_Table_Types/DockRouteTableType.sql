﻿IF NOT EXISTS (SELECT *
FROM sys.types
WHERE is_table_type = 1 AND name = 'DockRouteTableType')
BEGIN
CREATE TYPE [dbo].[DockRouteTableType] AS TABLE
(
	[ServiceOfferingName] [nvarchar](50) NOT NULL,
	[OriginTerminalCode]    NVARCHAR (3)  NOT NULL,
	[DestinationTerminalCode]    NVARCHAR (3) NOT NULL,
	[ServiceLevelCode] NVARCHAR (2) NOT NULL,
	[SeqNum] INT NOT NULL,
	[LegOriginTerminalCode]    NVARCHAR (3)  NOT NULL,
	[LegDestinationTerminalCode]    NVARCHAR (3) NOT NULL,
    INDEX IX NONCLUSTERED(ServiceOfferingName, OriginTerminalCode, DestinationTerminalCode, ServiceLevelCode)
)
END