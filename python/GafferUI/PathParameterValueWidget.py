##########################################################################
#  
#  Copyright (c) 2011-2012, Image Engine Design Inc. All rights reserved.
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#  
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#  
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
##########################################################################

import re

import IECore

import Gaffer
import GafferUI

class PathParameterValueWidget( GafferUI.ParameterValueWidget ) :

	def __init__( self, parameterHandler, **kw ) :
		
		self.__pathWidget = GafferUI.PathPlugValueWidget(
			parameterHandler.plug(),
			self._path(),
			pathChooserDialogueKeywords = self._pathChooserDialogueKeywords(),
		)
					
		GafferUI.ParameterValueWidget.__init__(
			
			self,
			self.__pathWidget,
			parameterHandler,
			**kw
			
		)
		
	def _path( self ) :
	
		return Gaffer.FileSystemPath( "/", filter = self._filter() )

	def _filter( self ) :
		
		return Gaffer.FileSystemPath.createStandardFilter()
		
	def _pathChooserDialogueKeywords( self ) :
	
		return {}
	
GafferUI.ParameterValueWidget.registerType( IECore.PathParameter.staticTypeId(), PathParameterValueWidget )
