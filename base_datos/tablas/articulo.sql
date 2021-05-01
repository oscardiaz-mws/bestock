USE [bestock]
GO

/****** Object:  Table [dbo].[Articulo]    Script Date: 4/12/2021 10:38:14 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Articulo](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](max) NOT NULL,
	[precio] [money] NOT NULL,
	[url] [nvarchar](max) NOT NULL,
	[tieneDescuento] [bit] NOT NULL,
	[descuento] [float] NOT NULL,
 CONSTRAINT [PK_Articulo] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[Articulo] ADD  CONSTRAINT [DF_Articulo_precio]  DEFAULT ((0)) FOR [precio]
GO

ALTER TABLE [dbo].[Articulo] ADD  CONSTRAINT [DF_Articulo_tieneDescuento]  DEFAULT ((0)) FOR [tieneDescuento]
GO

ALTER TABLE [dbo].[Articulo] ADD  CONSTRAINT [DF_Articulo_descuento]  DEFAULT ((0)) FOR [descuento]
GO


