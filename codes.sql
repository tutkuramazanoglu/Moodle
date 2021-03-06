USE [schoolDb]
GO
/****** Object:  Table [dbo].[admin]    Script Date: 16.4.2020 23:35:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[admin](
	[adminID] [int] NOT NULL,
	[adminName] [varchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[adminID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[course]    Script Date: 16.4.2020 23:35:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[course](
	[courseID] [int] NOT NULL,
	[courseName] [nvarchar](50) NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[courseStudent]    Script Date: 16.4.2020 23:35:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[courseStudent](
	[courseID] [int] NOT NULL,
	[studentID] [int] NOT NULL,
	[grade] [int] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[professor]    Script Date: 16.4.2020 23:35:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[professor](
	[professorID] [int] NOT NULL,
	[professorName] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_professor] PRIMARY KEY CLUSTERED 
(
	[professorID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[professorCourse]    Script Date: 16.4.2020 23:35:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[professorCourse](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[courseID] [int] NULL,
	[professor] [int] NULL,
 CONSTRAINT [PK_professorCourse] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[professorStudent]    Script Date: 16.4.2020 23:35:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[professorStudent](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[professorID] [int] NULL,
	[studentID] [int] NULL,
 CONSTRAINT [PK_professorStudent] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[student]    Script Date: 16.4.2020 23:35:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[student](
	[studentID] [int] NOT NULL,
	[studentName] [nvarchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[users]    Script Date: 16.4.2020 23:35:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[users](
	[userID] [int] NOT NULL,
	[userName] [nvarchar](50) NOT NULL,
	[userPassword] [nvarchar](50) NOT NULL,
	[userType] [int] NOT NULL
) ON [PRIMARY]

GO
INSERT [dbo].[course] ([courseID], [courseName]) VALUES (123, N'bio')
INSERT [dbo].[course] ([courseID], [courseName]) VALUES (25, N'java')
INSERT [dbo].[course] ([courseID], [courseName]) VALUES (26, N'c#')
INSERT [dbo].[course] ([courseID], [courseName]) VALUES (27, N'python')
INSERT [dbo].[course] ([courseID], [courseName]) VALUES (20, N'css')
INSERT [dbo].[courseStudent] ([courseID], [studentID], [grade]) VALUES (26, 12, 6)
INSERT [dbo].[courseStudent] ([courseID], [studentID], [grade]) VALUES (27, 12, 7)
INSERT [dbo].[courseStudent] ([courseID], [studentID], [grade]) VALUES (25, 12, 5)
INSERT [dbo].[courseStudent] ([courseID], [studentID], [grade]) VALUES (27, 13, 8)
INSERT [dbo].[courseStudent] ([courseID], [studentID], [grade]) VALUES (26, 12, 6)
INSERT [dbo].[professor] ([professorID], [professorName]) VALUES (30, N'zach')
INSERT [dbo].[professor] ([professorID], [professorName]) VALUES (31, N'tarki')
INSERT [dbo].[professor] ([professorID], [professorName]) VALUES (32, N'murat')
SET IDENTITY_INSERT [dbo].[professorCourse] ON 

INSERT [dbo].[professorCourse] ([ID], [courseID], [professor]) VALUES (3, 123, 30)
INSERT [dbo].[professorCourse] ([ID], [courseID], [professor]) VALUES (1002, 20, 30)
SET IDENTITY_INSERT [dbo].[professorCourse] OFF
INSERT [dbo].[student] ([studentID], [studentName]) VALUES (41, N'adrian')
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (1, N'tutku', N'tut', 1)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (2, N'zach', N'zac', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (3, N'hemat', N'hem', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (4, N'faiz', N'fai', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (1004, N'kana', N'kan', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (1004, N'kana', N'kan', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (1004, N'kana', N'kan', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (30, N'cameron', N'cam', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (11, N'utku', N'utk', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (12, N'yasin', N'yas', 3)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (1004, N'kana', N'kan', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (31, N'tarki', N'tar', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (30, N'zach', N'zac', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (33, N'hakan', N'hak', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (34, N'acun', N'acu', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (35, N'celik', N'cel', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (36, N'levetn', N'lev', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (37, N'serdar', N'ser', 2)
INSERT [dbo].[users] ([userID], [userName], [userPassword], [userType]) VALUES (41, N'adrian', N'dem', 3)
