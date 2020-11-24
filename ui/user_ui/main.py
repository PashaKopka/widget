<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>542</width>
    <height>432</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout_2">
    <item>
     <widget class="QScrollArea" name="widgets_area">
      <property name="verticalScrollBarPolicy">
       <enum>Qt::ScrollBarAlwaysOn</enum>
      </property>
      <property name="widgetResizable">
       <bool>true</bool>
      </property>
      <widget class="QWidget" name="scrollAreaWidgetContents">
       <property name="geometry">
        <rect>
         <x>0</x>
         <y>0</y>
         <width>497</width>
         <height>346</height>
        </rect>
       </property>
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <layout class="QVBoxLayout" name="widgets_layout">
          <item>
           <widget class="QPushButton" name="clock_widget_button">
            <property name="font">
             <font>
              <pointsize>14</pointsize>
              <weight>50</weight>
              <italic>false</italic>
              <bold>false</bold>
              <underline>false</underline>
              <strikeout>false</strikeout>
              <kerning>true</kerning>
             </font>
            </property>
            <property name="mouseTracking">
             <bool>false</bool>
            </property>
            <property name="tabletTracking">
             <bool>false</bool>
            </property>
            <property name="focusPolicy">
             <enum>Qt::StrongFocus</enum>
            </property>
            <property name="contextMenuPolicy">
             <enum>Qt::DefaultContextMenu</enum>
            </property>
            <property name="acceptDrops">
             <bool>false</bool>
            </property>
            <property name="toolTip">
             <string/>
            </property>
            <property name="statusTip">
             <string/>
            </property>
            <property name="whatsThis">
             <string/>
            </property>
            <property name="accessibleName">
             <string/>
            </property>
            <property name="accessibleDescription">
             <string notr="true"/>
            </property>
            <property name="layoutDirection">
             <enum>Qt::LeftToRight</enum>
            </property>
            <property name="autoFillBackground">
             <bool>true</bool>
            </property>
            <property name="text">
             <string>clock widget</string>
            </property>
            <property name="checkable">
             <bool>true</bool>
            </property>
            <property name="autoRepeat">
             <bool>false</bool>
            </property>
            <property name="autoExclusive">
             <bool>false</bool>
            </property>
            <property name="autoDefault">
             <bool>true</bool>
            </property>
            <property name="default">
             <bool>true</bool>
            </property>
            <property name="flat">
             <bool>false</bool>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </widget>
     </widget>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout">
      <property name="sizeConstraint">
       <enum>QLayout::SetMinimumSize</enum>
      </property>
      <item>
       <widget class="QPushButton" name="add_widget_button">
        <property name="font">
         <font>
          <pointsize>12</pointsize>
         </font>
        </property>
        <property name="text">
         <string>Add widget</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="del_widget_button">
        <property name="font">
         <font>
          <pointsize>12</pointsize>
         </font>
        </property>
        <property name="text">
         <string>Delete widget</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
